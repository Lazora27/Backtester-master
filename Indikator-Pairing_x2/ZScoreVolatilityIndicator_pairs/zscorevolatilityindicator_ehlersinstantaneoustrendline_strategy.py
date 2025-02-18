import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZScoreVolatilityIndicator_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZScoreVolatilityIndicator und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'ZScoreVolatilityIndicator': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
