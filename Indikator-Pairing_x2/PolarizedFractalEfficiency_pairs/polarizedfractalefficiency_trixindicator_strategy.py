import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedFractalEfficiency_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedFractalEfficiency und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'PolarizedFractalEfficiency': 1.0,
            'TRIXIndicator': 1.0
        })
    )
