import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HilbertTrendline': 1.0
        })
    )
