import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
