import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
