import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und FisherSignals
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'FisherSignals': 1.0
        })
    )
