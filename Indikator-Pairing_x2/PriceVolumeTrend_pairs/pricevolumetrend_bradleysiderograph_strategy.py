import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'BradleySiderograph': 1.0
        })
    )
