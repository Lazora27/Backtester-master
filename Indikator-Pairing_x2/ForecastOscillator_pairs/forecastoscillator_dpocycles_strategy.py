import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
