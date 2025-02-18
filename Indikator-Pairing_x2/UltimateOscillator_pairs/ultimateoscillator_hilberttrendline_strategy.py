import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'HilbertTrendline': 1.0
        })
    )
