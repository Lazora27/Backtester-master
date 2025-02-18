import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und DPOCycles
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'DPOCycles': 1.0
        })
    )
