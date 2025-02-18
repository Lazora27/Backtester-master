import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'SeasonalStrength': 1.0
        })
    )
