import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
