import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'SeasonalStrength': 1.0
        })
    )
