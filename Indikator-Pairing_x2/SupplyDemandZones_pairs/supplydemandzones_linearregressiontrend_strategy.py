import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
