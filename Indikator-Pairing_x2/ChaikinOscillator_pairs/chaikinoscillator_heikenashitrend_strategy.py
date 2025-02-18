import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
