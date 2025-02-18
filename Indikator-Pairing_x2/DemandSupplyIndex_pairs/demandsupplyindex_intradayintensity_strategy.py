import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
