import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_EhlersInstantaneousTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und EhlersInstantaneousTrend
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'EhlersInstantaneousTrend': 1.0
        })
    )
