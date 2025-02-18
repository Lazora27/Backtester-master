import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MarketFacilitationMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MarketFacilitationMomentum
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MarketFacilitationMomentum': 1.0
        })
    )
