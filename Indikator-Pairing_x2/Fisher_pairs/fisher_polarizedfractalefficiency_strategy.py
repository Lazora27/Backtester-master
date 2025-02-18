import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_PolarizedFractalEfficiency_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und PolarizedFractalEfficiency
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'PolarizedFractalEfficiency': 1.0
        })
    )
