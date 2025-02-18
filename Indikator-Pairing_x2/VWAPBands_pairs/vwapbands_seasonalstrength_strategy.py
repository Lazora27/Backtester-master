import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'SeasonalStrength': 1.0
        })
    )
