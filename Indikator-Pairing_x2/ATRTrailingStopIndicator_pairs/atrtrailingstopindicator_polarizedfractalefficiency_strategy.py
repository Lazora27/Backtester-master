import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ATRTrailingStopIndicator_PolarizedFractalEfficiency_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ATRTrailingStopIndicator und PolarizedFractalEfficiency
    """
    
    params = (
        ('indicators', {
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            },
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            }
        }),
        ('weights', {
            'ATRTrailingStopIndicator': 1.0,
            'PolarizedFractalEfficiency': 1.0
        })
    )
