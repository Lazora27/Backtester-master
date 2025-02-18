import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und NVISignals
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'NVISignals': 1.0
        })
    )
