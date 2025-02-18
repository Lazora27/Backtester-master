import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
