import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'SeasonalStrength': 1.0
        })
    )
