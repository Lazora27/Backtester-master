import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'VortexIndicator': 1.0
        })
    )
