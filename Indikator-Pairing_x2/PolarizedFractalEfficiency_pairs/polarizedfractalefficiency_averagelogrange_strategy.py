import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedFractalEfficiency_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedFractalEfficiency und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'PolarizedFractalEfficiency': 1.0,
            'AverageLogRange': 1.0
        })
    )
