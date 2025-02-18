import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_SupplyDemandLiquidityMap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und SupplyDemandLiquidityMap
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'SupplyDemandLiquidityMap': 1.0
        })
    )
