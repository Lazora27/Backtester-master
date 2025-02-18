import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AccelerationBands': 1.0
        })
    )
