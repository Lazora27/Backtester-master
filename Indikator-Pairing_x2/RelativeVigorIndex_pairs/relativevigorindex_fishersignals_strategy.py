import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
