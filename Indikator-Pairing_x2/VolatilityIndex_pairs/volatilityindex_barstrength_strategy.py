import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'BarStrength': 1.0
        })
    )
