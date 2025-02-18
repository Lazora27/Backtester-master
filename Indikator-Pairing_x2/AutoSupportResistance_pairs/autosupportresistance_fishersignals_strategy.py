import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und FisherSignals
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'FisherSignals': 1.0
        })
    )
