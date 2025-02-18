import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
