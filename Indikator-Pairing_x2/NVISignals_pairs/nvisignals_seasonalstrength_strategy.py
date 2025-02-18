import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SeasonalStrength': 1.0
        })
    )
