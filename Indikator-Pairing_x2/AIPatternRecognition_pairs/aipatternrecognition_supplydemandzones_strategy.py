import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
