import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
