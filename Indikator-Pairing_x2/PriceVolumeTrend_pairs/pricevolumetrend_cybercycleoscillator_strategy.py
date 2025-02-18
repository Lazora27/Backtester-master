import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
