import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und BarStrength
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'BarStrength': 1.0
        })
    )
