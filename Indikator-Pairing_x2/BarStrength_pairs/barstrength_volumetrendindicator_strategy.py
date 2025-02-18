import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
