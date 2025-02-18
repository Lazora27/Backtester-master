import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
