import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und CyberCycle
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'CyberCycle': 1.0
        })
    )
