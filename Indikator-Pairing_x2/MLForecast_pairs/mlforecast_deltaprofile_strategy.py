import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DeltaProfile': 1.0
        })
    )
