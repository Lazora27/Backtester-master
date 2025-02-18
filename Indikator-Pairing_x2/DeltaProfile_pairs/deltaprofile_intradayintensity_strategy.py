import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'IntradayIntensity': 1.0
        })
    )
