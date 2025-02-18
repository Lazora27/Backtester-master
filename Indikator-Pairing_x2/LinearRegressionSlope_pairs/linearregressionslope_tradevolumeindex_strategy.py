import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
