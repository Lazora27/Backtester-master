import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandLiquidityMap_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandLiquidityMap und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'SupplyDemandLiquidityMap': {
                'class': SupplyDemandLiquidityMap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandLiquidityMap'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'SupplyDemandLiquidityMap': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
