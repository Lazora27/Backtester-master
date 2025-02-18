import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'ModifiedATR': 1.0
        })
    )
