import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ZScoreVolatilityIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ZScoreVolatilityIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ZScoreVolatilityIndicator': {
                'class': ZScoreVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZScoreVolatilityIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ZScoreVolatilityIndicator': 1.0
        })
    )
