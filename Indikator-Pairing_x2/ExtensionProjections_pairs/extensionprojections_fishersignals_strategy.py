import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'FisherSignals': 1.0
        })
    )
