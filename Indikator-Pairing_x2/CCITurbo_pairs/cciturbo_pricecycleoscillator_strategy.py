import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
