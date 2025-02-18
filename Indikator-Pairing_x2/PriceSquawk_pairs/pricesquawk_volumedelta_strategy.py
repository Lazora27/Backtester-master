import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'VolumeDelta': 1.0
        })
    )
