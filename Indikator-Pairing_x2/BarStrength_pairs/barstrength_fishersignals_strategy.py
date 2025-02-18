import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und FisherSignals
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'FisherSignals': 1.0
        })
    )
