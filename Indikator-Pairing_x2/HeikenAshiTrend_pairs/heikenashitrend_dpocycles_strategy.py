import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und DPOCycles
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'DPOCycles': 1.0
        })
    )
