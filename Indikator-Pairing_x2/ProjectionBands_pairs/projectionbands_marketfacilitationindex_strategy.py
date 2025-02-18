import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
