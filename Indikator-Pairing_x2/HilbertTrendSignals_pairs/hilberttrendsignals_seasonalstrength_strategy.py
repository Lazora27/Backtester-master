import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'SeasonalStrength': 1.0
        })
    )
