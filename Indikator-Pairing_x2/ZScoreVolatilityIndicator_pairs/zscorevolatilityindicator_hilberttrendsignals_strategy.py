import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZScoreVolatilityIndicator_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZScoreVolatilityIndicator und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'ZScoreVolatilityIndicator': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
