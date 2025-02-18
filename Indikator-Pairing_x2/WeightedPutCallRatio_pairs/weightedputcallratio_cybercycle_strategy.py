import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und CyberCycle
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'CyberCycle': 1.0
        })
    )
